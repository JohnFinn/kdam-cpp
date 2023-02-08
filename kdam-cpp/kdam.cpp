#include "kdam.hpp"
#include <cstddef>
#include <cstdint>

extern "C" {
    void tqdm_init(uint8_t*, size_t);
    void tqdm_update(uint8_t*);
    void tqdm_drop(uint8_t*);
}

namespace kdam {

tqdm::tqdm(std::size_t total) {
    tqdm_init(reinterpret_cast<uint8_t*>(&_storage), total);
}

void tqdm::update() {
    tqdm_update(reinterpret_cast<uint8_t*>(&_storage));
}

tqdm::~tqdm() {
    tqdm_drop(reinterpret_cast<uint8_t*>(&_storage));
}

}
