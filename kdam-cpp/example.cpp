#include <thread>
#include "kdam.hpp"

int main() {
    std::size_t total = 500;
    kdam::tqdm foo(total);
    for (int i = 0; i < total; ++i) {
        using namespace std::chrono_literals;
        foo.update();
        std::this_thread::sleep_for(50ms);
    }
}
