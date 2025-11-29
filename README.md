# AlaIE
- author: Iawnix
- date: 2025-11-29

1. 参考Z. H. Zhang等人JCTC的工作[DOI: 10.1021/acs.jctc.7b01295]
2. 计算原理:
- $$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
- $$IE = KT[\ln\langle e^{\beta \Delta E^{a}_{int}}\rangle - \ln\langle e^{\beta \Delta E^{x}_{int}}\rangle]$$
- $$langle e^{\beta \Delta E^{x}_{int}}\rangle = \frac{1}{N} \sum_{i=1}^{N} e^{\beta \Delta E^{x}_{int}(t_{i})}$$  
- $$\Delta E^{x}_{int}(t_{i}) = E^{x}_{int}(t_{i}) - \langle E^{x}_{int}\rangle$$
- $$E_{int} = E^{vac}_{ele} + E^{vac}_{vdW}$$
# Install
- `conda create -n AlaIE python=3.10`
- `conda activate AlaIE`
- `pip install .`

# Usage
- `AlaIE -h`

# Test
## Linux
- `cd ./test`
- `./run.sh`
## windows
- `mkdir out`
- `AlaIE -AlaDecPath ./data/ -T 300 -out test.txt -debug True`

