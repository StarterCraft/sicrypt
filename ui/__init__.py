#coding=utf-8
from PySide6    import QtCore, QtGui, QtWidgets
from enum     import Enum
from typing   import Any, List, Dict, Tuple, Iterator, Union
from json     import load
from glob     import glob

from sicrypt      import SicryptComponent
from sicrypt      import deepget
from sicrypt      import app, ui, options, hardware


class SicryptUiTheme(dict):
    def __init__(self, name) -> None:
        super().__init__({'name': name})

        self.read()

    def __iter__(self) -> Iterator[Tuple[str, str]]:
        return iter(zip(
            self.componentList, 
            [self.__dict__[ck] for ck in self.componentList]))

    def read(self) -> None:
        'Чтение темы'
        self.componentList: List[str] = []

        try:
            load(open(f'theme/{self.name}/manifest.json', 'r', encoding = 'utf-8'))
        except:
            raise FileNotFoundError(f'Тема {self.name} не имеет файла manifest.json'
                'или он повреждён')

        with open(f'theme/{self.name}/manifest.json', 'r', encoding = 'utf-8') as f:
            #Прочесть displayName, style
            self.update(load(f))

        for styleSheetFile in glob(f'theme/{self.name}/*.qss'):
            targetName = styleSheetFile.split('\\')[-1][:-4]
            self.componentList.append(targetName)

            with open(styleSheetFile, 'r', encoding = 'utf-8') as f:
                self.update({targetName: f.read()})


class SicryptUiComponentType(Enum):
    Window = 2
    Dialog = 1
    Widget = 0


class SicryptUiComponent(SicryptComponent):
    'Создание униформизма между всеми компонентами интерфейса.'
    def __init__(
            self,
            name: str,
            cmType: SicryptUiComponentType,
            *args,
            displayName: str = '',
            loggerName: str = '',
            **kwargs
        ):
        super().__init__(
            name, 
            *args,
            displayName = displayName,
            loggerName = loggerName,
            **kwargs
        )

        self.cmType = cmType

        ui().add(self)

        self.setupUi(self)
        self.defaultSize = QtCore.QSize(
            *deepget(
                options().ui,
                f'{self.name}.size',                
                default = (self.minimumSize().width(), self.minimumSize().height())
            )
        )
        self.resize(self.defaultSize)

        self.theme: str = deepget(options().ui, f'{self.name}.theme', default = 'default')

    def setupUi(self, *args):
        super().setupUi(*args)

    def interconnect(self):
        super().interconnect()

    def bind(self):
        super().bind()

    def updateUi(self):
        super().updateUi()

    def cleanUi(self):
        super().cleanUi()

    def show(self, **kwargs):
        super().show(**kwargs)

    def close(self):
        self.cleanUi()
        super().close()

    def isVisible(self) -> bool:
        return super().isVisible()





class SicryptUi(SicryptComponent):
    def __init__(self) -> None:
        super().__init__('ui')

        self.components: List[SicryptUiComponent] = []

    def __getitem__(self, name: str) -> SicryptUiComponent:
        try:
            return [c for c in self.components if (c.name == name)][0]
        except IndexError:
            raise KeyError(f'Компонент GUI {name} не найден или не зарегистрирован')

    def __iter__(self) -> Iterator[SicryptUiComponent]:
        return iter(self.components)

    def setupUi(self):

        for c in self: 
            self.logger.debug(f'{c.name} size: {c.size()}')

        self.interconnect()
        self.bind()
        self.loadThemes()
        self.themize()

    def interconnect(self):
        for component in self:
            component.interconnect()

        self.logger.debug(
            'Взаимосвязывание сигналов в интерфейсе выполнено'
        )
        
    def bind(self):
        for component in self:
            component.bind()

        self.logger.debug(
            'Глобальная привязка сочетаний клавиш выполнена'
        )

    def updateUi(self):
        for component in self:
            component.updateUi()

        self.logger.debug(
            'Интерфейс полностью обновлён'
        )

    def cleanUi(self):
        for component in self:
            component.cleanUi()

        self.logger.debug(
            'Интерфейс полностью очищен'
        )

    def show(self):
        for component in self:
            if (component.name in options().ui.keys()):
                self.showComponent(component)

    def showComponent(self, component: SicryptUiComponent):
        if (options().ui[component.name].get('onLaunch', False)):
            component.show()

            self.logger.debug(
                f'Компонент {component.name} отображён согласно настройкам'
            )

    def add(self, component: SicryptUiComponent):
        self.components.append(component)
        setattr(self, component.name, component)

        self.logger.debug(
            f'Компонент {component.name} зарегистрирован'
        )

    def remove(self, component: Union[SicryptUiComponent, str]):
        if (isinstance(component, SicryptUiComponent)):
            self.components.remove(component)
            delattr(self, component.name)

        if (isinstance(component, str)):
            self.components.remove(self[component.name])
            delattr(self, component)

        self.logger.debug(
            f'Компонент {component.name} недоступен'
        )

    def loadThemes(self):
        self.themes: List[SicryptUiTheme] = []

        for themePath in glob('theme/*'):
            themeName = themePath.split('\\')[-1]
            theme = SicryptUiTheme(themeName)
            self.themes.append(theme)

            self.logger.debug(
                f'Загружена тема {theme.displayName} ({themeName}, '
                f'{len(theme.componentList)} QSS)'
            )

    def getTheme(self, name: str) -> SicryptUiTheme:
        return [t for t in self.themes if (t.name == name)][0]

    def themize(self, theme: str = ''):
        self.themizeApp(theme)

        for component in self:
            self.themizeComponent(component)

    def themizeApp(self, theme: str = None):
        appTheme = self.getTheme(
            theme if theme else deepget(options().ui, 'app.theme', 'default')
        )
        
        app().setStyle(appTheme.style)

        appQss = appTheme.get('app', '')
        app().setStyleSheet(appQss)

        self.logger.debug(f'Тема {appTheme.name}: установлен глобальный QSS длиной {len(appQss)}')
        self.logger.debug(f'Тема {appTheme.name}: установлен глобальный QStyle {appTheme.style}')

    def themizeComponent(self, c: SicryptUiComponent, theme: str = ''):
        theme = self.getTheme(
            theme if theme else deepget(options().ui, f'{c.name}.theme', 'default')
        )

        c.theme = theme.name

        self.logger.debug(f'Тема {theme.name} установлена для компонента {c.name}')

        cQss = theme.get(c.name, self.getTheme('default').get(c.name, ''))
        if (cQss):
            c.setStyleSheet(cQss)
            self.logger.debug(f'Тема {theme.name}: установлен QSS для {c.name} длиной {len(cQss)}')

        for target, styleSheet in theme:
            subName = '.'.join(target.split('.')[1:])

            if (len(target.split('.')) > 1 and 
                hasattr(c, subName)):
                getattr(c, subName).setStyleSheet(styleSheet)

                self.logger.debug(f'Тема {theme.name}: '
                    f'установлен QSS для {target} длиной {len(theme[target])}'
                )

    def isVisible(self) -> bool:
        return any(c.isVisible() for c in self.components)
