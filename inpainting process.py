import cv2
#1.resim
src = cv2.imread("Images/ISIC_0000042.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 1.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme islemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamayı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye baglı olarak orijinal 1.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 1.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/1.jpg",dst)
cv2.destroyAllWindows()


#2.resim
src = cv2.imread("Images/ISIC_0000043.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 2.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım..
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 2.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 2.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/2.jpg",dst)
cv2.destroyAllWindows()


#3.resim
src = cv2.imread("Images/ISIC_0000095.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 3.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 3.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 3.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/3.jpg",dst)
cv2.destroyAllWindows()


#4.resim
src = cv2.imread("Images/ISIC_0000115.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 4.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 4.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 4.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/4.jpg",dst)
cv2.destroyAllWindows()


#5.resim
src = cv2.imread("Images/ISIC_0000138.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 5.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 5.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 5.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/5.jpg",dst)
cv2.destroyAllWindows()


#6.resim
src = cv2.imread("Images/ISIC_0000191.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 6.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 6.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 6.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/6.jpg",dst)
cv2.destroyAllWindows()


#7.resim
src = cv2.imread("Images/ISIC_0000214.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 7.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 7.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 7.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/7.jpg",dst)
cv2.destroyAllWindows()


#8.resim
src = cv2.imread("Images/ISIC_9228573.jpg")
src=cv2.resize(src,(500,500))
print( src.shape )
cv2.imshow("Orjinal 8.Resim" , src )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Orjinal resmi grayscale'ye dönüştürdüm.
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
cv2.imshow("GrayScale",grayScale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kernel için morfolojik filtreleme işlemi yaptım.
kernel = cv2.getStructuringElement(1,(17,17))

# saç sınır çizgilerini bulmak için gri tonlamalı görüntü üzerinde blackHat filtrelemesini gerçekleştirdim.
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat morphologyEx islemi",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# inpaint işlemine hazırlanırken saç konturlarını yoğunlaştırdım.
ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
print( thresh2.shape )
cv2.imshow("Thresholded Maskesi",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# maskeye bağlı olarak orijinal 8.görüntüde inpaint işlemi yaptım.
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imshow("InPaint kullanilmis 8.resim",dst)
cv2.waitKey(0)
cv2.imwrite("outputs/8.jpg",dst)
cv2.destroyAllWindows()













