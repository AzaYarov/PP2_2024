def solve(heads, legs):
    chickens = int((legs - 4*heads) / - 2)
    rabbits = int(heads - chickens)

    print(f"rabiits: {rabbits}, chikens: {chickens} ")

heads = 35
legs = 94

