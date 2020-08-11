import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)