def challenge(facts, schema):
    result = set()
    for element in facts:
        if element[-1]:
            if (element[1], 'cardinality', 'one') in schema:
                for item in result:
                    if element[0:2] == item[0:2]:
                        result.remove(item)
                        break
                result.add(element)
            elif (element[1], 'cardinality', 'many') in schema:
                result.add(element)
    return result
