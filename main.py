from optimizer import TransportOptimizer
from io_handler import IOHandler
from algorithms import Algorithms
from visualization import Visualizer


def run():
    obj, io, algo, viz = TransportOptimizer(), IOHandler(), Algorithms(), Visualizer()

    if not io.load_csv(obj):
        print("Failed to initialize. Check distance.csv.")
        return

    while True:
        print("\n--- Transport System (CSV Loaded) ---")
        print("1. Find Optimized Route")
        print("2. Reload CSV")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            print(f"Cities: {', '.join(obj.locations)}")
            start = input("Enter Start City: ").strip()
            route, dist = algo.nearest_neighbor(obj, start)

            if route:
                print(f"\nOptimal Route: {' -> '.join(route)}")
                print(f"Total Distance: {dist}")
                viz.plot(obj, route)
            else:
                print("City not found!")
        elif choice == "2":
            io.load_csv(obj)
        elif choice == "3":
            break


if __name__ == "__main__":
    run()