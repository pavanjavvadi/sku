from sku_backend.core.models import SKU, Category, Department, Location, SubCategory
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database with metadata and SKU data"

    def handle(self, *args, **kwargs):
        # Seed location and related data
        self.seed_location_data()
        # Seed SKU data
        self.seed_sku_data()

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

    def seed_location_data(self):
        location_department_category_subcategory = [
            ("Perimeter", "Bakery", "Bakery Bread", "Bagels"),
            ("Perimeter", "Bakery", "Bakery Bread", "Baking or Breading Products"),
            ("Perimeter", "Bakery", "Bakery Bread", "English Muffins or Biscuits"),
            ("Perimeter", "Bakery", "Bakery Bread", "Flatbreads"),
            ("Perimeter", "Bakery", "In Store Bakery", "Breakfast Cake or Sweet Roll"),
            ("Perimeter", "Bakery", "In Store Bakery", "Cakes"),
            ("Perimeter", "Bakery", "In Store Bakery", "Pies"),
            ("Perimeter", "Bakery", "In Store Bakery", "Seasonal"),
            ("Center", "Dairy", "Cheese", "Cheese Sauce"),
            ("Center", "Dairy", "Cheese", "Specialty Cheese"),
            ("Center", "Dairy", "Cream or Creamer", "Dairy Alternative Creamer"),
            ("Center", "Dairy", "Cream or Creamer", "Whipping Creams"),
            ("Center", "Dairy", "Cultured", "Cottage Cheese"),
            ("Center", "Dairy", "Refrigerated Baking", "Refrigerated Breads"),
            ("Center", "Dairy", "Refrigerated Baking", "Refrigerated English Muffins and Biscuits"),
            ("Center", "Dairy", "Refrigerated Baking", "Refrigerated Hand Held Sweets"),
            ("Center", "Dairy", "Refrigerated Baking", "Refrigerated Pie Crust"),
            ("Center", "Dairy", "Refrigerated Baking", "Refrigerated Sweet Breakfast Baked Goods"),
            ("Perimeter", "Deli and Foodservice", "Self Service Deli Cold", "Beverages"),
            ("Perimeter", "Deli and Foodservice", "Service Deli", "Cheese All Other"),
            ("Perimeter", "Deli and Foodservice", "Service Deli", "Cheese American"),
            ("Perimeter", "Floral", "Bouquets and Cut Flowers", "Bouquets and Cut Flowers"),
            ("Perimeter", "Floral", "Gifts", "Gifts"),
            ("Perimeter", "Floral", "Plants", "Plants"),
            ("Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"),
            ("Center", "Frozen", "Frozen Bake", "Breakfast Cake or Sweet Roll Frozen"),
            ("Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Entrees"),
            ("Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Sandwich"),
            ("Center", "Frozen", "Frozen Breakfast", "Frozen Egg Substitutes"),
            ("Center", "Frozen", "Frozen Breakfast", "Frozen Syrup Carriers"),
            ("Center", "Frozen", "Frozen Desserts or Fruit and Toppings", "Pies Frozen"),
            ("Center", "Frozen", "Frozen Juice", "Frozen Apple Juice"),
            ("Center", "Frozen", "Frozen Juice", "Frozen Fruit Drink Mixers"),
            ("Center", "Frozen", "Frozen Juice", "Frozen Fruit Juice All Other"),
            ("Center", "GM", "Audio Video", "Audio"),
            ("Center", "GM", "Audio Video", "Video DVD"),
            ("Center", "GM", "Audio Video", "Video VHS"),
            ("Center", "GM", "Housewares", "Bedding"),
            ("Center", "GM", "Housewares", "Candles"),
            ("Center", "GM", "Housewares", "Collectibles and Gifts"),
            ("Center", "GM", "Housewares", "Flashlights"),
            ("Center", "GM", "Housewares", "Frames"),
            ("Center", "GM", "Insect and Rodent", "Indoor Repellants or Traps"),
            ("Center", "GM", "Insect and Rodent", "Outdoor Repellants or Traps"),
            ("Center", "GM", "Kitchen Accessories", "Kitchen Accessories"),
            ("Center", "GM", "Laundry", "Bleach Liquid"),
            ("Center", "GM", "Laundry", "Bleach Powder"),
            ("Center", "GM", "Laundry", "Fabric Softener Liquid"),
            ("Center", "GM", "Laundry", "Fabric Softener Sheets"),
            ("Center", "Grocery", "Baking Ingredients", "Dry or Canned Milk"),
            ("Center", "Grocery", "Baking Ingredients", "Food Coloring"),
            ("Center", "Grocery", "Spices", "Salt Cooking or Edible or Seasoned"),
            ("Center", "Grocery", "Spices", "Salt Substitute"),
            ("Center", "Grocery", "Spices", "Seasoning Dry"),
            ("Center", "Grocery", "Stuffing Products", "Stuffing Products"),
            ("Perimeter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"),
            ("Perimeter", "Seafood", "Other Seafood", "All Other Seafood"),
            ("Perimeter", "Seafood", "Other Seafood", "Prepared Seafood Entrees"),
            ("Perimeter", "Seafood", "Other Seafood", "Seafood Salads"),
            ("Perimeter", "Seafood", "Other Seafood", "Smoked Fish"),
            ("Perimeter", "Seafood", "Other Seafood", "Seafood Breading Sauces Dips"),
        ]

        for (
            location_name,
            department_name,
            category_name,
            subcategory_name,
        ) in location_department_category_subcategory:
            location, _ = Location.objects.get_or_create(location_name=location_name)
            department, _ = Department.objects.get_or_create(department_name=department_name, location=location)
            category, _ = Category.objects.get_or_create(category_name=category_name, department=department)
            SubCategory.objects.get_or_create(subcategory_name=subcategory_name, category=category)

    def seed_sku_data(self):
        sku_data = [
            (1, "SKUDESC1", "Perimeter", "Bakery", "Bakery Bread", "Bagels"),
            (2, "SKUDESC2", "Perimeter", "Deli and Foodservice", "Self Service Deli Cold", "Beverages"),
            (3, "SKUDESC3", "Perimeter", "Floral", "Bouquets and Cut Flowers", "Bouquets and Cut Flowers"),
            (4, "SKUDESC4", "Perimeter", "Deli and Foodservice", "Service Deli", "All Other"),
            (5, "SKUDESC5", "Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"),
            (6, "SKUDESC6", "Center", "Grocery", "Crackers", "Rice Cakes"),
            (7, "SKUDESC7", "Center", "GM", "Audio Video", "Audio"),
            (8, "SKUDESC8", "Center", "GM", "Audio Video", "Video DVD"),
            (9, "SKUDESC9", "Perimeter", "GM", "Housewares", "Bedding"),
            (10, "SKUDESC10", "Perimeter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"),
            (11, "SKUDESC11", "Perimeter", "Seafood", "Other Seafood", "All Other Seafood"),
            (12, "SKUDESC12", "Perimeter", "Seafood", "Other Seafood", "Prepared Seafood Entrees"),
            (13, "SKUDESC13", "Perimeter", "Seafood", "Other Seafood", "Seafood Salads"),
            (14, "SKUDESC14", "Perimeter", "Bakery", "Bakery Bread", "Bagels"),
            (15, "SKUDESC15", "Perimeter", "Deli and Foodservice", "Self Service Deli Cold", "Beverages"),
            (16, "SKUDESC16", "Perimeter", "Floral", "Bouquets and Cut Flowers", "Bouquets and Cut Flowers"),
            (17, "SKUDESC17", "Perimeter", "Deli and Foodservice", "Service Deli", "All Other"),
            (18, "SKUDESC18", "Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"),
        ]

        for sku_id, sku_name, location_name, department_name, category_name, subcategory_name in sku_data:
            # Get or create Location, Department, Category, SubCategory, and SKU
            location, _ = Location.objects.get_or_create(location_name=location_name)
            department, _ = Department.objects.get_or_create(department_name=department_name, location=location)
            category, _ = Category.objects.get_or_create(category_name=category_name, department=department)
            subcategory, _ = SubCategory.objects.get_or_create(subcategory_name=subcategory_name, category=category)

            SKU.objects.get_or_create(
                sku_name=sku_name, location=location, department=department, category=category, subcategory=subcategory
            )
