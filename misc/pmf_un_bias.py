
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, _ in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf


def UnbiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, _ in pmf.Items():
        new_pmf.Mult(x, 1.0/x)
    new_pmf.Normalize()
    return new_pmf
