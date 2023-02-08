#pragma once
#include <cstddef>
#include <type_traits>

namespace kdam {

class tqdm {
public:
    tqdm(std::size_t total);

    tqdm(const tqdm&)=delete;
    tqdm& operator=(const tqdm&)=delete;
    tqdm(tqdm&&)=delete;
    tqdm& operator=(tqdm&&)=delete;

    void update();

    ~tqdm();

private:
    // TODO calculate constants in compile time
    std::aligned_storage_t<240, 8> _storage;
};

}
