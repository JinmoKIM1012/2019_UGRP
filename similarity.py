import jellyfish


def lv_sim(test_str, check_str):
    return 1.0 - jellyfish.levenshtein_distance(test_str, check_str) / max(len(test_str), len(check_str))


def hm_sim(test_str, check_str):
    return 1.0 - jellyfish.hamming_distance(test_str, check_str) / max(len(test_str), len(check_str))


def jw_sim(test_str, check_str):
    return jellyfish.jaro_winkler(test_str, check_str)


def sim(test_str, check_str):
    return (lv_sim(test_str, check_str) +  hm_sim(test_str, check_str) + jw_sim(test_str, check_str)) / 3
