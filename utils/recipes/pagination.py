import math

def make_pagination_range(
    page_range, #total de paginas
    qty_pages, #quantidade que deve aparecer na tela
    current_page, #pagina atual
):
    middle_range = math.ceil(qty_pages / 2) #calcula o meio
    start_range = current_page - middle_range #calcula o inicio
    stop_range = current_page + middle_range #calcula o fim
    total_pages = len(page_range)  

    start_range_offset = abs(start_range) if start_range < 0 else 0 #ajusta o inicio se for negativo

    if start_range < 0: 
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]
    return{
        'pagination': pagination,
        'page range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,    
    }

