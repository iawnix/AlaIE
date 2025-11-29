# AlaIE
- author: Iawnix
- date: 2025-11-29

1. 参考Z. H. Zhang等人JCTC的工作[DOI: 10.1021/acs.jctc.7b01295]
2. 计算原理:
$$
IE = KT[ln<e^{\beta \Delta E^{a}_{int}}> - ln<e^{\beta \Delta E^{x}_{int}}>]
<e^{\beta \Delta E^{x}_{int}}> = \frac{1}{N} \sum^{N}_{i=1} e^{\beta \Delta E^{x}_{int}(t_{i})}
\Delta E^{x}_{int}(t_{i}) = E^{x}_{int}(t_{i}) - <E^{x}_{int}>
E_{int} = E^{vac}_{ele} + E^{vac}_{vdW}
$$
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

