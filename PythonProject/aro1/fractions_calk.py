def get_items():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        znak = oper.get().strip()
    except Exception:
        znak = ''
    match znak:
        case '+':
            n = n1 * d2 + n2 * d1
            d = d1 * d2
        case '-':
            n = n1 * d2 - n2 * d1
            d = d1 * d2
        case '*':
            n = n1 * n2
            d = d1 * d2
        case '/':
            n = n1 * d2
            d = d1 * n2
    nod = math.gcd(n, d)
    n = n // nod
    d = d // nod
    int_p = ''
    if n > d:
        int_p = n // d
        n = n % d
    int_part['text'] = str(int_p)
    num3['text'] = str(n)
    den3['text'] = str(d)