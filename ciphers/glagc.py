'Convertion of Cyrillic Russian text to Glagolic Russian text and backwards'

from main import Cipher

class RuCyrillicToGlagolic(Cipher):
    '''
    A cipher implementing convertion of Cyrillic Russian text
    to Glagolic Russian text and backwards.
    '''
    cyrillicUppercase = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
        'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    cyrillicLowercase = [
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    glagolicUppercase = [
        'Ⰰ', 'Ⰱ', 'Ⰲ', 'Ⰳ', 'Ⰴ', 'Ⰵ', 'Ⱖ', 'Ⰶ', 'Ⰸ', 'Ⰻ', 'Ⰺ', 'Ⰽ', 'Ⰾ', 'Ⰿ', 'Ⱀ', 'Ⱁ', 'Ⱀ',
        'Ⱃ', 'Ⱄ', 'Ⱅ', 'Ⱆ', 'Ⱇ', 'Ⱈ', 'Ⱌ', 'Ⱍ', 'Ⱎ', 'Ⱋ', 'Ⱏ', 'ⰟⰉ', 'Ⱐ', 'ⰟⰅ', 'Ⱓ', 'Ⱑ']

    glagolicLowercase = [
        'ⰰ', 'ⰱ', 'ⰲ', 'ⰳ', 'ⰴ', 'ⰵ', 'ⱖ', 'ⰶ', 'ⰸ', 'ⰻ', 'ⰺ', 'ⰽ', 'ⰾ', 'ⰿ', 'ⱀ', 'ⱁ', 'ⱀ',
        'ⱃ', 'ⱄ', 'ⱅ', 'ⱆ', 'ⱇ', 'ⱈ', 'ⱌ', 'ⱍ', 'ⱎ', 'ⱋ', 'ⱏ', 'ⱏⰹ', 'ⱐ', 'ⱏⰵ', 'ⱓ', 'ⱑ']


    def __init__(self):
        Cipher.__init__(self, True, 
            'Convertion between Cyrillic and Glagolic Russian text', __name__, 'simple')


    def encrypt(self, text: str, encoding: str) -> str:
        'Cyrillic text to Glagolic text'
        chars = list(text)
        result = ''

        for i in range(len(list(text))):
            if chars[i] in self.cyrillicUppercase: result += self.glagolicUppercase[self.cyrillicUppercase.index(chars[i])]
            elif chars[i] in self.cyrillicLowercase: result += self.glagolicLowercase[self.cyrillicLowercase.index(chars[i])]
            else: result += chars[i]

        return result


    def decrypt(self, text: str, encoding: str) -> str:
        'Glagolic text to Cyrillic text'
        chars = list(text)
        result = ''

        for i in range(len(list(text))):
            if chars[i] in self.glagolicUppercase: result += self.cyrillicUppercase[self.glagolicUppercase.index(chars[i])]
            elif chars[i] in self.glagolicLowercase: result += self.cyrillicLowercase[self.glagolicLowercase.index(chars[i])]
            else: result += chars[i]

        return result
