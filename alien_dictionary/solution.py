

from collections import defaultdict, deque

def alien_order(words):
   
    if not words:
        return ""
    
  
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}

 
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
      
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break 
    
    
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    order = []
    
    while queue:
        if len(queue) > 1:
          
            return ""
        
        current = queue.popleft()
        order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
 
    if len(order) != len(in_degree):
        return ""  
    
    return "".join(order)