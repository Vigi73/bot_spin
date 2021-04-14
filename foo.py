import pyautogui as bot
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def determining_the_catch():
    """распазнаем текст садка"""
    img = bot.screenshot('fish.png', region=(580, 270, 334, 167))
    answer = pytesseract.image_to_string(img, lang='rus').split('\n')[:4]
    return answer


def sale_fish():
    pass


def travel():
    bot.click(601, 343)


def fish_tank(check):
    """Орабатываем садок"""
    if im := bot.locateOnScreen('img/tank.bmp', region=(562, 226, 68, 31)):
        bot.keyUp('ctrlright')
        result = determining_the_catch()
        # print(result[1], '(зачетная)' in result[1].split())

        if check:
            if '(зачетная)' in result[1].split():
                pass
            else:
                bot.hotkey('shift', 'e')
                bot.sleep(.2)
                bot.press('space')
                return -1
        return result


def foods():
    """Кушаем"""
    if im := bot.locateOnScreen('img/foods.bmp', region=(455, 704, 39, 105)):
        bot.keyUp('g')
        bot.click(624, 848)
        bot.sleep(.3)
        bot.click(1153, 603)
        bot.sleep(.3)
        bot.click(1197, 346)
        bot.sleep(.3)
        bot.keyDown('g')
        return 1

