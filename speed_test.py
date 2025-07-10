import asyncio
import ipaddress
import time

PORTS = [80, 443]

def generate_ips(cidr, limit=100):
    net = ipaddress.ip_network(cidr)
    ips = []
    for ip in net.hosts():
        ips.append(str(ip))
        if len(ips) >= limit:
            break
    return ips

async def test_tcp(ip, port, timeout=3):
    start = time.time()
    try:
        reader, writer = await asyncio.open_connection(ip, port, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return ip, port, time.time() - start
    except:
        return ip, port, None

async def main():
    cidrs = ['104.16.0.0/12', '162.159.0.0/16']
    ips_to_test = []
    for cidr in cidrs:
        ips_to_test.extend(generate_ips(cidr, limit=100))

    tasks = []
    for ip in ips_to_test:
        for port in PORTS:
            tasks.append(test_tcp(ip, port))

    results = await asyncio.gather(*tasks)
    success_results = [r for r in results if r[2] is not None]
    success_results.sort(key=lambda x: x[2])

    with open('speed_results.txt', 'w') as f:
        f.write("测试成功的 IP 和延迟 (最快前 20):\n")
        for ip, port, delay in success_results[:20]:
            line = f"{ip}:{port} 延迟 {delay*1000:.2f} ms\n"
            print(line.strip())
            f.write(line)

if __name__ == "__main__":
    asyncio.run(main())
