use kdam::{tqdm, Bar, BarExt};
use std::mem;
use std::ptr;

#[no_mangle]
pub static BAR_SIZE: usize = mem::size_of::<Bar>();

#[no_mangle]
pub static BAR_ALIGN: usize = mem::align_of::<Bar>();

#[no_mangle]
pub unsafe extern "C" fn tqdm_init(obj: *mut u8, total: usize) {
    std::ptr::write(obj as *mut Bar, Bar::new(total));
}

#[no_mangle]
pub unsafe extern "C" fn tqdm_update(obj: *mut u8) {
    (*(obj as *mut Bar)).update(1);
}

#[no_mangle]
pub unsafe extern "C" fn tqdm_drop(obj: *mut u8) {
    std::ptr::drop_in_place(obj as *mut Bar);
}
