input = """0 27 5409930 828979 4471 3 68524 170"""
parsed_input = list(map(int, input.split(" ")))


mem = {}


def blink(current, blinks_left=6):
    if blinks_left == 0:
        return current
    result = []
    for x in current:
        if x in mem:
            result += mem[x]
            continue
        if x == 0:
            result += [1]
            continue
        x_len = len(str(x))
        if x_len % 2 == 0:
            half = x_len // 2
            mem[x] = [int(str(x)[:half]), int(str(x)[half:])]
            result += mem[x]
            continue
        mem[x] = [x * 2024]
        result += mem[x]
    return blink(result, blinks_left - 1)


print("part 1", len(blink(parsed_input, 25)))

parsed_input = tuple(map(int, input.split(" ")))


mem = {}


def blink2(current, amount=6):
    if current in mem:
        cache = mem[current]
        cache_size = len(cache)
        if cache_size >= amount:
            print("wow")
            return cache[amount - 1]
        return blink2(cache[-1], amount - cache_size)
    if amount == 0:
        return current

    if len(current) == 1:
        item = current[0]
        if item == 0:
            return blink2((1,), amount - 1)
        item_len = len(str(item))
        if item_len % 2 == 0:
            half = item_len // 2
            result = (int(str(item)[:half]), int(str(item)[half:]))
            mem[current] = mem.get(current, []) + [result]
            return blink2(result, amount - 1)
        result = (item * 2024,)
        mem[current] = mem.get(current, []) + [result]
        return blink2(result, amount - 1)

    result = ()
    for x in current:
        result += blink2((x,), amount)
    mem[current] = mem.get(current, []) + [result]
    return result


parsed_input = list(map(int, input.split(" ")))


mem = {}


def blink2(stone, blinks_left=25):
    key = (stone, blinks_left)
    if blinks_left == 0:
        return 1
    if key in mem:
        return mem[key]
    if stone == 0:
        return blink2(1, blinks_left - 1)
    stone_len = len(str(stone))
    if stone_len % 2 == 0:
        half = stone_len // 2
        result = blink2(int(str(stone)[:half]), blinks_left - 1) + blink2(
            int(str(stone)[half:]), blinks_left - 1
        )
        mem[key] = result
        return result
    result = blink2(stone * 2024, blinks_left - 1)
    mem[key] = result
    return result


parsed_input = tuple(map(int, input.split(" ")))


print("part 2", sum(blink2(x, 75) for x in parsed_input))
