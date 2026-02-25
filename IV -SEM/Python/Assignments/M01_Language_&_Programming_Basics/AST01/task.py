def Ticket_Pricing(n: int) -> int:
    if n < 10:
        return 10
    elif n < 100:
        return 20
    else:
        return 15




if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
