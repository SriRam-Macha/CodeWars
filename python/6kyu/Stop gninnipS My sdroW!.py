def spin_words (sentence):
    final_sentence = " "
    words = [str(i) for i in sentence.split(" ")]
    for i in range( len(words)):
      if len(words[i]) >= 5 :
        words[i] = words[i][::-1]
    return final_sentence.join(words)