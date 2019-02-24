import opUrl

address = "http://tenshi.spb.ru/anime-ost/"
info = opUrl.url_web(address)

while True:
    num = 1
    # muestra la lista extraida de la pagina
    for dir in info:
        print(str(num)+" -> "+dir)
        num=num + 1
    opUrl.url_back(address)
    # It is asking for next directory
    directory = input("Choose a number. forward  --> / <--- backward. A letter \"q\" : ")
    if directory == "q":
        address = opUrl.url_back(address)
        info = opUrl.url_web(address)
        print("<--- "+address)
    else:
        try:
            # checking if the url has a file or it is another directory.
            if info[int(directory)-1].find(".mp3", 0, len(info[int(directory)-1])) != -1:
                print("Downloading...")
                # address = address + info[int(directory)-1]
                opUrl.url_download(address, info[int(directory) - 1])
            else:
                # adding piece of url.
                address = address + info[int(directory)-1]
                print("Moving to -->: "+address)
                info = opUrl.url_web(address)
        except NameError as err:
            print("Error: "+str(err))

