class AirMap():
    def __init__(self,routes={}):
        self.routes = routes
        return

    def add_route(self, start, destination):
        if self.routes.get(start):
            self.routes[start].append(destination)
        else:
            self.routes[start] = [destination]
        return

    def print_all_routes(self, start, destination):
        path = []
        visited = set()
        all = []
        def helper(start, destination, path, visited, all):
            path.append(start)
            visited.add(start)
            if start == destination:
                all.append(list(path))
            else:
                for route in self.routes[start]:
                    if route not in visited:
                        helper(route,destination, path, visited, all)
            path.pop()
            visited.remove(start)
        helper(start,destination,path,visited,all)                
        return all


airmap1 = AirMap()
airmap1.add_route("A","B")
airmap1.add_route("B","A")
airmap1.add_route("A","C")
airmap1.add_route("C","A")
airmap1.add_route("A","D")
airmap1.add_route("D","A")
airmap1.add_route("B","C")
airmap1.add_route("C","B")
airmap1.add_route("B","D")
airmap1.add_route("D","B")
print(airmap1.routes)
print(airmap1.print_all_routes("C","D"))

