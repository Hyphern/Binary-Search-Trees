from AVLTree import AVLTree
from Heap import MinHeap
from TreeNode import TreeNode
from datetime import datetime, timedelta

class PriceTracker:
    def __init__(self):
        """
        Initialize a new PriceTracker to track prices and their statistics.
        
        Attributes:
            _price_history: AVLTree to store price data with timestamps
            _recent_min_prices: MinHeap to track recent minimum prices
            _recent_max_prices: MinHeap to track recent maximum prices
            _time_to_min_node: Dictionary mapping time to min node in the heap
            _time_to_max_node: Dictionary mapping time to max node in the heap
            _latest_time: The latest time for which price data has been recorded
            _window_sum: Sum of prices in the current 10-day window
            _window_count: Count of prices in the current 10-day window
        """
        self._price_history = AVLTree()
        self._recent_min_prices = MinHeap()
        self._recent_max_prices = MinHeap()
        self._time_to_min_node = {}
        self._time_to_max_node = {}
        self._latest_time = None
        self._window_sum = 0.0
        self._window_count = 0 
    
    def _inorder_traversal(self, node, start, end, result):
        """Helper method for range query to traverse the tree in-order and collect results
        
        Args:
            node: The current node in the AVL tree
            start: The start of the range (inclusive)
            end: The end of the range (inclusive)
            result: List to store the results of the range query
        """
        if node is None:
            return

        if node.key > start:
            self._inorder_traversal(node.left, start, end, result)
        
        if start <= node.key <= end:
            result.append((node.key, node.value))

        if node.key < end:
            self._inorder_traversal(node.right, start, end, result)
    
    def _get_range_query(self, start, end):
        """Perform a range query on the AVL tree to get price data
        
        Args:
            start: The start of the range (inclusive)
            end: The end of the range (inclusive)

        Returns:
            list: [(time, (price, ten_day_min, ten_day_max, ten_day_avg)), ...] ordered by time
        """
        result = []
        self._inorder_traversal(self._price_history.root, start, end, result)
        result.sort(key=lambda x: x[0])
        return result
    
    def add_price(self, time: datetime, price: float):
        """
        Add a new price data point with its timestamp.
        
        Args:
            time: datetime object representing when price was recorded
            price: float representing the price value
        """
        if self._latest_time is None:
            ten_day_min = price
            ten_day_max = price
            ten_day_avg = price
            
            self._price_history.insert(time, (price, ten_day_min, ten_day_max, ten_day_avg))
            
            min_node = TreeNode(price)
            max_node = TreeNode(-price)

            self._recent_min_prices.insert_node(min_node)
            self._recent_max_prices.insert_node(max_node)

            self._time_to_min_node[time] = min_node
            self._time_to_max_node[time] = max_node

            self._window_sum = price
            self._window_count = 1
            self._latest_time = time
            return

        new_window_start = time - timedelta(days=10)
        outdated_times = []

        for old_time in list(self._time_to_min_node.keys()):
            if old_time < new_window_start:
                outdated_times.append(old_time)

        for outdated_time in outdated_times:
            min_node_to_remove = self._time_to_min_node[outdated_time]
            max_node_to_remove = self._time_to_max_node[outdated_time]

            outdated_price = min_node_to_remove.key

            self._window_sum -= outdated_price
            self._window_count -= 1

            try:
                self._recent_min_prices.delete_node(min_node_to_remove)
                self._recent_max_prices.delete_node(max_node_to_remove)
            except KeyError:
                pass

            del self._time_to_min_node[outdated_time]
            del self._time_to_max_node[outdated_time]

        new_min_node = TreeNode(price)
        new_max_node = TreeNode(-price)
        
        self._recent_min_prices.insert_node(new_min_node)
        self._recent_max_prices.insert_node(new_max_node)

        self._time_to_min_node[time] = new_min_node
        self._time_to_max_node[time] = new_max_node
        
        self._window_sum += price
        self._window_count += 1
        
        if self._recent_min_prices.root is None:
            ten_day_min = price
            ten_day_max = price
            ten_day_avg = price
        else:
            ten_day_min = self._recent_min_prices.root.key
            ten_day_max = -self._recent_max_prices.root.key
            ten_day_avg = self._window_sum / self._window_count

        self._price_history.insert(time, (price, ten_day_min, ten_day_max, ten_day_avg))
        self._latest_time = time
    
    def get_price_data(self, start: datetime, end: datetime):
        """
        Get price data within a specified time range.
        
        Args:
            start: datetime object representing start of range (inclusive)
            end: datetime object representing end of range (inclusive)
            
        Returns:
            list: [(time, (price, ten_day_min, ten_day_max, ten_day_avg)), ...] ordered by time
        """
        return self._get_range_query(start, end)