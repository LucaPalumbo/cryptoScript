def general_hastad(ciphertexts, moduli, pad_array, const_array=(), e=3, eps=1/8):
    if not(len(ciphertexts) == len(moduli) == len(pad_array) == len(const_array) == e):
        raise RuntimeError("Moduli and ciphertext arrays have to be equal in length, and contain at least as many elements as e")

    '''
    Initialization with placeholders
    ciphertexts: ciphertext array
    T_array: Chinese Remainder Theorem coefficients
    moduli: Modulus array
    pad_array: Linear coefficient of padding applied to the message during encryption
    const_array: constant pad added to message during encryption (optional)
    '''
    T_array = [Integer(0)]*e
    crt_array = [Integer(0)]*e
    polynomial_array = []

    for i in range(e):
        crt_array = [0]*e
        crt_array[i] = 1
        T_array[i] = Integer(crt(crt_array,moduli))

    G.<x> = PolynomialRing(Zmod(prod(moduli)))
    for i in range(e):
        polynomial_array += [T_array[i]*((pad_array[i]*x+const_array[i])^e - Integer(ciphertexts[i]))] #Representation of polynomial f(x) = (A*x + b) ^ e - C where (A*x + b) is the padding polynomial

    g = sum(polynomial_array).monic()  #Creates a monic polynomial from the sum of the individual polynomials
    roots = g.small_roots(epsilon=eps)
    return roots[0] if len(roots) >= 1 else -1
