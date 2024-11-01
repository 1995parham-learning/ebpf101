from bcc import BPF

def main():
    with open('source.c', 'r') as f:
        program = f.read()

    print(f'source: {program}')
    b = BPF(text=program)
    syscall = b.get_syscall_fnname('execve')
    b.attach_kprobe(event=syscall, fn_name=b"hello")

    b.trace_print()



if __name__ == "__main__":
    main()
