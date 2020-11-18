from python_imagesearch.imagesearch import imagesearch

pos = imagesearch("./images/timemanip.png")
if pos[0] != -1:
    print("found")
else:
    print("not found")
