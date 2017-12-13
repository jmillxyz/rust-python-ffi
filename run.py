from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int foo(int);
""")

C = ffi.dlopen("./target/debug/librust_python_ffi.dylib")

# doubles an int
print(C.foo(9))


