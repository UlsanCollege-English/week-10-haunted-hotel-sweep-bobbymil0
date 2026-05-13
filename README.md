[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/I7NCKCh8)
# Week 10 Coding #8: Haunted Hotel Sweep

## Summary

This assignment models a haunted hotel as an undirected graph where each area is a node and each hallway, stairway, or door is an edge.  
`get_neighbors` reads the adjacency list safely, and `has_path` checks whether one area can be reached from another.  
`bfs_order` performs a breadth-first sweep, visiting nearby areas first by using a queue.  
`dfs_order` performs a depth-first sweep, exploring one path as far as possible first by using a stack.  
The `visited` set matters because it prevents repeated visits, avoids infinite loops in cycles, and keeps each traversal efficient.

---

## Approach

- Used `graph.get(area, [])` in `get_neighbors` so missing areas return an empty list instead of raising an error.
- Checked path existence with BFS so the search explores connected areas level by level until the target is found or the reachable component is exhausted.
- Built `has_path` and `bfs_order` with `collections.deque` and `popleft()` to maintain true queue behavior.
- Built `dfs_order` with a Python list as a stack and iterated through `reversed(neighbors)` so the final traversal still follows the graph's original neighbor order.
- Added a `visited` set so repeated areas are skipped and cycles cannot trap the traversal in an infinite loop.
- Implemented the stretch function by reusing the BFS traversal result and counting how many unique areas were visited.

---

## Complexity

### `get_neighbors`

- Time: `O(1)` average
- Space: `O(1)`
- Why: Dictionary lookup is constant time on average, and the function only returns the stored list reference or an empty list.

### `has_path`

- Time: `O(V + E)`
- Space: `O(V)`
- Why: In the worst case, BFS visits every area once and checks every edge from the reachable component. The queue and `visited` set can each grow to include up to all vertices.

### `bfs_order`

- Time: `O(V + E)`
- Space: `O(V)`
- Why: BFS visits each area once and examines each adjacency list once. The queue, visited set, and output list can each store up to all reachable vertices.

### `dfs_order`

- Time: `O(V + E)`
- Space: `O(V)`
- Why: DFS also visits each area once and examines each edge once. The stack, visited set, and output list can each grow to the size of the reachable component.

### Stretch: `count_reachable_areas` if completed

- Time: `O(V + E)`
- Space: `O(V)`
- Why: It reuses the BFS traversal result, so it has the same traversal cost and stores the reachable order before counting it.

---

## Edge-Case Checklist

Check the cases your code handles.

- [x] empty graph
- [x] missing start area
- [x] missing target area
- [x] `start == target`
- [x] graph with a cycle
- [x] disconnected graph
- [x] area with no neighbors

The main tricky case was cycles. Tracking visited areas prevents duplicate work and protects the traversal from looping forever.

---

## Tests Added

- Added `test_bfs_order_area_with_no_neighbors`
- Added `test_traversals_handle_cycle_without_revisiting`
- Kept and passed the provided tests for missing nodes, disconnected components, empty graphs, and the stretch function

---

## Known Limitations

```text
No known limitations.
```

---

## Assistance & Sources

AI used? Y

If yes, explain what it helped with:

- explanations
- debugging
- test ideas

Other sources used:

- `HOMEWORK_BRIEF.md`
