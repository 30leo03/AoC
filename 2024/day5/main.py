
from collections import defaultdict, deque


def rules_top_sort(rules, updates):
    for idx, update in enumerate(updates):
        relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

        # had 2 google thisdedi3608
        adj = defaultdict(list)
        in_degree = defaultdict(int)
        for node in update:
            in_degree[node] = 0

        for a, b in relevant_rules:
            adj[a].append(b)
            in_degree[b] += 1

        queue = deque([node for node in update if in_degree[node] == 0])
        sorted_nodes = []

        while queue:
            node = queue.popleft()
            sorted_nodes.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_nodes) != len(update):
            continue

        position_map = {node: pos for pos, node in enumerate(sorted_nodes)}
        update_sorted = sorted(update, key=lambda x: position_map.get(x, 0))
        updates[idx] = update_sorted

    return updates


def got_updates(rules, updates, changed):
    rules = [tuple(map(int, line.strip().split("|"))) for line in rules.strip().splitlines()]
    updates = [list(map(int, line.strip().split(","))) for line in updates.strip().splitlines()]
    original_updates = [list(u) for u in updates]

    return [u for u, o in zip(rules_top_sort(rules, updates), original_updates) if (u != o) == changed]


def main(file):
    with open(file, 'r') as f:
        upper_part, lower_part = f.read().strip().split("\n\n")

    print(sum(u[len(u) // 2] for u in got_updates(upper_part, lower_part, changed=False)))
    print(sum(u[len(u) // 2] for u in got_updates(upper_part, lower_part, changed=True)))


if __name__ == '__main__':
    main("input.txt")
