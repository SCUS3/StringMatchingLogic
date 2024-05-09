_scores[item] = fuzz.partial_ratio(reference[0].lower(), item.lower())
    return similarity_s