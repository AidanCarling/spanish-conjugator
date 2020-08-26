# -*- coding: iso-8859-15 -*-
def indicitive_present(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "o"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "o"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "o"
            return conjugation
            
    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "as"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "es"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "es"
            return conjugation

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "a"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "e"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "e"
            return conjugation

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "amos"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "emos"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "imos"
            return conjugation

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "áis"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "éis"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "ís"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "an"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "en"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "en"
            return conjugation