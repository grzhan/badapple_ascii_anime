#-*- coding: utf-8 -*-
# Image 库即PIL，是用来进行数字图像处理的Python库
import Image

# color = 'MNHQ$OC?7>!:-;.'
# 字符映射，将对应的像素根据其灰度映射成不同的字符，比如 `M` 代表黑色， ' '空格代表白色等
color = ' NHQ$OC?7>!:-  '

def make_char_img(img):
	""" 将已经预处理好的图片根据color生成字符字符串，存放到 pic_str 变量中 """
	pix = img.load()
	pic_str = ''
	width, height = img.size
	for h in xrange(height):
		for w in xrange(width):
			pic_str += color[int(pix[w,h]) * 14 /255]
		pic_str += '\n'
	return pic_str

def preprocess(img_name):
	""" 预处理: 通过使用PIL库里的函数将图片打开并重新缩放大小"""
	img = Image.open(img_name)
	w, h = img.size
	m = max(img.size)
	# 修改 delta 可以更改图片的大小，分母越大图片越大。
	delta = m / 40.0
	w, h = int(w/delta), int(h/delta)
	img = img.resize((w,h))
	img = img.convert('L')
	return img

def save_to_file(filename, pic_str):
	""" 将生成的图片载入到 filename 中"""
	outfile = open(filename,'w')
	outfile.write(pic_str)
	outfile.close()

def main():
	""" 这是主函数,相当于 C 里的 int main() """
	# 预处理 'ncg.jpg' 图片，把处理好的图片放入 img 变量中
	img = preprocess('nerv.jpg')
	# 生成图片字符串
	pic_str = make_char_img(img)
    # 保存字符串到 foo.txt 中
	save_to_file('foo.txt', pic_str)

if __name__ == '__main__':
	main()
