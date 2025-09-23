from PriceTracker import PriceTracker
from datetime import datetime

class MarketTracker:
    def __init__(self):
        """
        Initialize a new MarketTracker to track prices of multiple assets.

        Attributes:
            _asset_trackers: Dictionary mapping asset names to their respective PriceTracker instances
        """
        self._asset_trackers = {}
    
    def add_price(self, name: str, time: datetime, price: float):
        """
        Add a new price data point for the specified asset.
        
        Args:
            name: str representing the asset symbol (e.g., "NVDA")
            time: datetime object representing when price was recorded
            price: float representing the price value
        """
        if name not in self._asset_trackers:
            self._asset_trackers[name] = PriceTracker()

        self._asset_trackers[name].add_price(time, price)
    
    def get_price_data(self, name: str, start: datetime, end: datetime):
        """
        Get price data for a specific asset within a specified time range.
        
        Args:
            name: str representing the asset symbol (e.g., "NVDA")
            start: datetime object representing start of range (inclusive)
            end: datetime object representing end of range (inclusive)
            
        Returns:
            list: [(time, (price, ten_day_min, ten_day_max, ten_day_avg)), ...] ordered by time
            
        Raises:
            KeyError: If the specified asset symbol is not found
        """
        if name not in self._asset_trackers:
            raise KeyError(f"Asset '{name}' not found in market tracker")

        return self._asset_trackers[name].get_price_data(start, end)