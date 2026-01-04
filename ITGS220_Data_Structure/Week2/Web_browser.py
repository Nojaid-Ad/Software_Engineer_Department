class WebPage:
    def __init__(self, url):
        self.url = url
        self.previous = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.head = None
        self.current_page = None

    def visit_page(self, url):
        new_page = WebPage(url)
        if not self.head:
            self.head = new_page
            self.current_page = new_page
        else:
            self.current_page.next = new_page
            new_page.previous = self.current_page
            self.current_page = new_page

    def go_back(self):
        if self.current_page.previous:
            self.current_page = self.current_page.previous

    def go_forward(self):
        if self.current_page.next:
            self.current_page = self.current_page.next

    def print_history(self):
        current = self.head
        while current:
            print(current.url)
            current = current.next


# Example Usage
if __name__ == "__main__":
    browser = BrowserHistory()
    browser.visit_page("https://www.google.com")
    browser.visit_page("https://en.wikipedia.org/wiki/Linked_list")
    browser.visit_page("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    print("Browser History:")
    browser.print_history()

    print("\nGo back one page:")
    browser.go_back()
    print("Current page:", browser.current_page.url)

    print("\nGo forward one page:")
    browser.go_forward()
    print("Current page:", browser.current_page.url)
