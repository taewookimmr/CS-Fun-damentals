def solution(words, queries):
    limit = 10000+1
    trie = [({}, {}) for _ in range(limit)] ## forward, reverse
    for word in words:
        for i, _word_ in [[0, word], [1, word[::-1]]]:
            dic = trie[len(word)][i]
            for c in _word_:
                dic['count'] = dic.get('count', 0) + 1
                dic.setdefault(c, {})
                dic = dic[c]
    answer = []
    for querie in queries:
        m = 1 if querie[0] == '?' else 0 # reverse or forward
        dic = trie[len(querie)][m] 
        if m : querie=querie[::-1]
        for q in querie:
            if q == '?': 
                answer.append(dic.get('count', 0))

                break
            if q not in dic: 
                answer.append(0)
                break
            dic = dic[q]
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))