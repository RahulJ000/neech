def TowerOfHanoi(n, s_pole, d_pole, i_pole):
    if n == 1:
        print("move disc from pole", s_pole, "to pole", d_pole)
        return
    TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
    print("move disc", n, "from pole", s_pole, "to pole", d_pole)
    TowerOfHanoi(n-1, i_pole, d_pole, s_pole)

n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
