import base64
import json
from result import Result
from operation_type import Operation
from itertools import islice

def get_result(op_type, message, passphrase):
    st = get_message_bytes(op_type, message)
    cph = bytes(passphrase, 'utf-8')

    chunks = get_chunked_string(st, cph, None)
    final_str = get_merged_string(chunks, cph, op_type)

    return Result(op_type, final_str)

def get_chunked_string(str_arr, cph_arr, tmp_chunk_list):
    chunks = tmp_chunk_list if tmp_chunk_list is not None else []
    index = sum(len(c) for c in chunks)
    chunk = list(islice(str_arr, index, index + len(cph_arr)))

    if len(chunk) == 0:
        return tmp_chunk_list

    chunks.append(chunk)
    return get_chunked_string(str_arr, cph_arr, chunks)

def get_merged_string(chunks, cph, op):
    bytes_list = []

    for c in chunks:
        for i in range(0, len(c)):
            bytes_list.append(c[i] + cph[i] if op == Operation.ENCODE else c[i] - cph[i])

    arr = bytearray(bytes_list)
    return base64.b64encode(arr).decode('UTF-8') if op == Operation.ENCODE else arr.decode('UTF-8') 

def get_message_bytes(op, str):
    return bytes(str, 'utf-8') if op == Operation.ENCODE else base64.b64decode(str)
