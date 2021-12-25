def pred(model,arr):

    m = model.predict([arr])

    return 0 if m <0.5 else 1
