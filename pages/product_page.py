from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # TODO B1.3: name, unit_price, quantity, add_to_cart_button
        self.name = page.get_by_test_id("product-name")
        self.unit_price = page.get_by_test_id("unit-price")
        self.quantity = page.get_by_test_id("quantity")
        self.add_to_cart_button = page.get_by_test_id("add-to-cart")
        # Find the data-test values with DevTools (F12) or: playwright codegen https://practicesoftwaretesting.com

    def add_to_cart(self, quantity: int = 1):
        if quantity != 1:
            self.quantity.fill(str(quantity))

        self.add_to_cart_button.click()
        return self

    def price(self) -> float:
        # TODO B1.4: unit price as a float
        price_text = self.unit_price.inner_text()
        return float(price_text.replace("$", "").replace(",", "").strip())
