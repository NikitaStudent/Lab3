import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def open_image():
    Tk().withdraw()
    image_path = askopenfilename(title="Выберите изображение", filetypes=[("Image files)", "*.jpg;*.jpeg;*.png;*.bmp")])

    if not image_path:
        print("Вы не выбрали изображение")
        return

    image = cv2.imread(image_path)

    if image is None:
        print("Ошибка открытия изображение")
        return

    gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    resiza_gray_image = cv2.resize(gray_image, (300,300))
    resiza_original_image = cv2.resize(image, (300, 300))

    cv2.imshow('Оригинальное изображение', image)
    cv2.imshow('Черно-белое изображение', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_image = image_path.rsplit('.', 1)[0] + '_gray_image.jpg'
    cv2.imwrite(save_image, gray_image)
    print(f'Черно-белая фотография сохранена как {save_image}')

open_image()