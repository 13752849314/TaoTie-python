# Created by 敖鸥 at 2022/8/9
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter = 'abcdefghjkmnpqrstuvwxy'
_number = ''.join(map(str, range(3, 10)))

# print(_letter, '\n', _number)
init_chars = ''.join((_letter, _number))


# print(init_chars)

def create_image(
        size=(80, 32),
        chars=init_chars,
        img_type='png',
        mode='RGB',
        bg_color=(255, 255, 255),
        fg_color=(0, 0, 255),
        font_size=15,
        font_type='HGH1_CNKI.ttf',
        length=5,
        draw_lines=True,
        n_line=(1, 2),
        draw_points=True,
        point_chance=2):
    """
    生成验证码图片
    :param size: 图片大小
    :param chars: 字符集合
    :param img_type: 图片格式
    :param mode: 图片模式
    :param bg_color: 背景色
    :param fg_color: 前景色
    :param font_size: 字体大小
    :param font_type: 字体
    :param length: 字符个数
    :param draw_lines: 是否画干扰线
    :param n_line: 干扰线条数的范围
    :param draw_points: 是否画干扰点
    :param point_chance: 干扰点出现的概率 -> [0, 100]
    :return: (PIL Image实例, 验证码图片中的字符串)
    """
    width, height = size
    # 创建图形
    img = Image.new(mode, size, bg_color)
    # 创建画笔
    draw = ImageDraw.Draw(img)

    def get_chars():
        """验证码字符串"""
        return random.sample(chars, length)

    def create_line():
        """绘制干扰线条"""
        line_num = random.randint(*n_line)
        for i in range(line_num):
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))

            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        """绘制干扰点"""
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        """绘制验证码字符"""
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)
        font = ImageFont.truetype(font_type, font_size)
        _, _, font_width, font_height = font.getbbox(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                  strs, font=font, fill=fg_color)

        return ''.join(c_chars)

    def img2str(IMG: Image.Image, fmt=img_type):
        """image to base64-str"""
        from io import BytesIO
        import base64
        out_buffer = BytesIO()
        IMG.save(out_buffer, format=fmt)
        byte_data = out_buffer.getvalue()
        base64_str = base64.b64encode(byte_data).decode('utf-8')
        return f'data:image/{fmt};base64,' + base64_str

    if draw_lines:
        create_line()
    if draw_points:
        create_points()
    strs = create_strs()

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    # 创建扭曲
    img = img.transform(size, Image.Transform.PERSPECTIVE, params)
    # 滤镜，边界加强（阈值更大）
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    base64_str = img2str(img, img_type)
    return img, strs, base64_str


# if __name__ == '__main__':
#     img1, strs1, S = create_image()
#     print(img1)
#     print(strs1)
#     img1.show()
#     print(S)
