def insults():
    insults = ["Bum","Idiots","Exploded-pigs of the world"]
    body_parts = ["Your leg looks like a ","Your leg looks like the "]
    insult = insults.random() + body_parts.random()
    return insult
print(insults)
