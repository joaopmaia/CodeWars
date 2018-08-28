def song_decoder(song): 
    aux = song.replace("WUB", " ") 
    aux = aux.strip()
    g = "  "
    while g in aux:
        aux = aux.replace(g, " ")
    print (aux)
 
    return aux