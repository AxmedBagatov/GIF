from PIL import Image
frames = []
for frame_number in range(1, 8):
 # Открываем изображение каждого кадра.
 frame = Image.open(f'LEV{frame_number}.jpg')
 # Добавляем кадр в список с кадрами.
 frames.append(frame)
# Берем первый кадр и в него добавляем оставшееся кадры.
frames[0].save(
 'result.gif',
 save_all=True,
 append_images=frames[1:], # Срез который игнорирует первый кадр.
 optimize=True,
 duration=2000,
 loop=0
)
