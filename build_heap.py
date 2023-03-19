# python3


def build_heap(data):
    swaps = []
    n=len(data)
    for i in range(n // 2, -1, -1):
        down(i, data, swaps)
    
    return swaps

def down(i, data, swaps):
    n=len(data)
    indekss = i

    left = 2*i + 1
    if left < n and data[left] < data[indekss]:
        indekss = left

    right = 2*i + 2
    if right < n and data[right] < data[indekss]:
        indekss = right
    
    if i != indekss:
        swaps.append((i, indekss))
        data[i], data[indekss] = data[indekss], data[i]
        down(indekss, data, swaps)
    

def main():
    
    inputs = input()
    if 'I' in inputs:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps), end=' ')
        for i, j in swaps:
            print(i, j, end=' ')
    elif 'F' in inputs:
        file = input()
        file = "tests/" + file
        if 'a' not in file:
            open_file = open(file)
            n = int(open_file.readline())
            inp = open_file.readline()
            open_file.close()
            m = inp.split(sep=" ")
            m2 = []
            for i in m:
                m2.append(int(i))

            assert len(m2) == n
            swaps = build_heap(m2)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
    
if __name__ == "__main__":
    main()
