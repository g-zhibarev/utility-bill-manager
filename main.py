paid_services = {}
all_services = set()

with open('receipts.txt', 'r', encoding='utf-8-sig') as file:
    for receipt in file:
        receipt_split = receipt.split('_')
        service = receipt_split[0]
        all_services.add(service)
        month = receipt_split[1].split('.')[0]
        if month not in paid_services:
            paid_services[month] = {
                'main': [{'service': service, 'receipt': receipt}],
                'all_paid_services': []
            }
        else:
            paid_services[month]['main'].append({'service': service, 'receipt': receipt})

with open('чеки_по_папкам.txt', 'w', encoding='utf-8') as file:
    for month, services in paid_services.items():
        for service in services['main']:
            receipt_val = service.get('receipt', None)
            file.write(f'/{month}/{receipt_val}')
            paid_services[month]['all_paid_services'].append(service.get('service', None))

    file.write('\nне оплачены:\n')
    for month, services in paid_services.items():
        c_services = services['all_paid_services'].copy()
        set_services = set(c_services)
        services_only_in_all_services = all_services.difference(set_services)
        if not services_only_in_all_services:
            continue
        file.write(f'{month}:\n')
        for service in services_only_in_all_services:
            file.write(f'{service}\n')
