
# 验证码识别环境安装

### 环境搭建

> 基于linux/mac、Python

1. 安装Python图像库

```
	pip install Pillow
```

2. 安装Python库Pytesseract

```
	pip install pytesseract
```

3. 安装Python库tesseract

```
	pip install tesseract
```

4. 安装leptonica

> 下载地址：http://www.leptonica.com/download.html

```
	./configure
	make
	make install
```

5. 安装tesseract-ocr

> 下载地址：https://github.com/tesseract-ocr/tesseract

```
	./autogen.sh
	CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib" ./configure
	make
	make install
```

安装完成后，再下载[tessdata](https://github.com/tesseract-ocr/tessdata)，将其放置于tessdata目录。

