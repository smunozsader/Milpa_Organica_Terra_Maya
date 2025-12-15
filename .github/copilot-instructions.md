# Terra Maya Orgánica - AI Coding Agent Instructions

## Project Context
This is an agricultural productivity modeling project for **Terra Maya Orgánica**, an organic poultry farm in Yucatán, Mexico. The codebase models a technified organic milpa system (intercropped corn/beans/squash) scaled to 250 ha under irrigation.

**Business Goal**: Calculate crop yields to support self-sufficiency in poultry feed (corn fodder) and commercial sales (Jamapa beans, squash seeds).

## Core Architecture

### Single-File Calculator Pattern
- Main logic in [`ilpa_productividad.py`](ilpa_productividad.py) - a standalone Python script with embedded documentation
- **NOT** a multi-module system - all calculations in one file for easy sharing with agronomists
- Output format: Direct console prints, no persistent storage or APIs

### Domain-Specific Calculations
Based on SPCM (Sistema de Producción Continua de Maíz) research validated in Yucatán's limestone soils:
- **Pocetas system**: 22,000 planting holes/ha with substrate mix (chicken manure + coconut husk)
- **Polycropping**: 3 corn + 2 bean + 0.5 squash seeds per hole (intercropping pattern)
- **3 cycles/year**: Enabled by drip irrigation + fertigation in tropical climate (no frost)

## Key Conventions

### Variable Naming (Spanish Agricultural Terms)
- `pocetas_por_ha` = planting holes per hectare (not "pockets")
- `rend_*` prefix = rendimiento (yield), e.g., `rend_maiz_anual`
- `plantas_*_ha` = established plants per hectare after survival rate
- Use Spanish for domain terms; English for code structure (`for`, `if`, etc.)

### Editable Parameters Section
**Always maintain** the top block (lines 4-17) as user-modifiable:
```python
# Parámetros editables
pocetas_por_ha = 22000
semillas_maiz_por_poceta = 3
...
```
Agronomists adjust these values directly - treat as configuration interface.

### Yield Calculations
- Per-plant yields (`rend_*_por_planta_ciclo`) are calibrated to SPCM research targets:
  - Corn: 3.5 t/ha/cycle → ~0.000066 t/plant (52,800 plants/ha)
  - Bean: 1.3 t/ha/cycle → ~0.000037 t/plant
  - Squash: Based on fruit-to-seed conversion (10% seed weight)
- **Critical**: Annual yield = `plants/ha × yield/plant × 3 cycles`

## Development Workflows

### Running Calculations
```powershell
# No virtual environment needed - uses system Python
python ilpa_productividad.py
```
Expected output format:
```
=== PRODUCTIVIDAD MILPA TECNIFICADA ===
Plantas/ha: Maíz 52800, Frijol 35200, Calabaza 8800
Rendimiento anual (t/ha): Maíz 10.5, Frijol 3.9, Calabaza 12.0
...
```

### Testing Changes
- Modify parameters → run script → verify output matches agronomic logic
- Cross-reference results with `terra_maya_conversacion.txt` (baseline assumptions)
- No automated tests - validation via domain expert review

## Reference Materials

### Supporting Documents (Read-Only Context)
- [`terra_maya_conversacion.txt`](terra_maya_conversacion.txt): Project rationale, SPCM research summary, and yield targets
- `2025. maiz continuo/*.pdf`: SPCM scientific papers from CICY researchers (Larqué Saavedra et al.)
- `2025. folletos web site pollos/`: Terra Maya Orgánica marketing materials

### Critical Assumptions to Preserve
1. **80% survival rate** - conservative for direct organic seeding
2. **3 cycles/year** - validated by Yucatán's year-round growing season
3. **Limestone soil (litosol)** - requires substrate-filled pocetas, not standard tillage

## Common Modifications

### Adjusting Crop Mix
To change seeding rates (e.g., more beans, less squash):
1. Edit `semillas_*_por_poceta` values
2. Verify `plantas_*_ha` calculations update correctly
3. Check `supervivencia` still applies uniformly (or split by crop if needed)

### Scaling to Full 250 ha
Replace `ha_lote = 20` with target area. Note: Script currently shows Phase 1 (20 ha); full deployment data in conversation file.

### Adding New Crops
Follow pattern:
```python
semillas_CULTIVO_por_poceta = X
plantas_CULTIVO_ha = pocetas_por_ha * semillas_CULTIVO_por_poceta * supervivencia
rend_CULTIVO_por_planta_ciclo = Y  # Calibrate to research
rend_CULTIVO_anual = plantas_CULTIVO_ha * rend_CULTIVO_por_planta_ciclo * ciclos_por_ano
```

## Expected Future Enhancements

### Cost Analysis Integration
- **Source data**: See [`costo_pocetas.txt`](costo_pocetas.txt) for initial capital costs (~$239,000 MXN/ha)
- Cost breakdown: Excavation ($150k/ha), substrate ($44k/ha), drip irrigation ($45k/ha)
- **Implementation pattern**: Add cost parameters to editable section, calculate ROI and payback period
- Example addition:
```python
# Costos (MXN/ha)
costo_excavacion_ha = 150000
costo_sustrato_ha = 44000
costo_riego_ha = 45000
# Calculate total investment and per-ton production cost
```

### Multi-Year Projections
- Model yield improvements from soil buildup (year 2+ with biofábricas)
- Account for substrate degradation/replenishment cycles
- Project revenue streams: poultry feed (internal), Jamapa beans, squash seeds (external sales)
- Consider SADER subsidy scenarios for capital costs

### Export Formats for Business Planning
- **CSV export**: Annual yields by crop and total revenue for spreadsheet analysis
- **Excel integration**: Formatted tables with cost/benefit ratios for stakeholder reports
- **Example implementation**:
```python
import csv
with open('reporte_anual.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Cultivo', 'Plantas/ha', 'Rend t/ha/año', 'Total 20 ha'])
```

## Calculation Validation Rules

### Realistic Yield Constraints
- **Corn max**: 10.5 t/ha/year (3.5 t/cycle × 3) - validated by SPCM in optimal conditions
- **Bean max**: 4.5 t/ha/year (1.5 t/cycle × 3) - upper bound for intercropped organic systems
- **Squash warning**: If `rend_calabaza_anual > 15 t/ha`, flag as unrealistic for Yucatán climate
- **Survival rate range**: 0.6-0.9 (below 60% indicates seeding/soil problems; above 90% unlikely in direct seeding)

### Input Validation Patterns
Add these checks before calculations:
```python
# Validate pocetas density
if pocetas_por_ha < 15000 or pocetas_por_ha > 30000:
    print(f"⚠️ ADVERTENCIA: Densidad {pocetas_por_ha} pocetas/ha fuera de rango típico (15k-30k)")

# Validate survival
if supervivencia < 0.6 or supervivencia > 0.9:
    print(f"⚠️ ADVERTENCIA: Supervivencia {supervivencia*100}% inusual para siembra directa")
```

### Cross-Crop Consistency
- Total seeds per poceta should match physical space: `(maíz + frijol + calabaza) × seed_size < poceta_volume`
- Corn:bean ratio typically 3:2 or 2:1 in traditional milpa - flag if bean > corn plants

### Edge Cases to Handle
1. **Zero cycles**: If `ciclos_por_ano < 1`, system reverts to traditional milpa (document this mode)
2. **Partial hectares**: Script currently uses `ha_lote = 20`; ensure calculations work for fractional ha (test plots)
3. **Missing irrigation**: Without fertigation, reduce `ciclos_por_ano` to 1 and yields to traditional levels

## Output Formatting Guidance

### Console Output Standards
Current format is stakeholder-friendly. When enhancing:
- Keep Spanish headers: `=== PRODUCTIVIDAD MILPA TECNIFICADA ===`
- Use thousand separators for large numbers: `{value:,.0f}` instead of `{value:.0f}`
- Add units explicitly: `(t/ha)`, `(plantas/ha)`, `(MXN)`

### Progressive Enhancement Pattern
```python
# Basic: Current implementation
print(f"Rendimiento anual (t/ha): Maíz {rend_maiz_anual:.1f}")

# Enhanced: Add totals and comparisons
print(f"Rendimiento anual (t/ha): Maíz {rend_maiz_anual:.1f} (+{mejora_vs_tradicional:.0f}% vs milpa tradicional)")

# Advanced: Tabular format for multiple scenarios
print(f"{'Cultivo':<15} {'t/ha/año':>10} {'Total 20 ha':>12} {'Valor MXN':>12}")
```

### Business Report Templates
For stakeholder presentations, generate:
1. **Summary table**: Crop yields, revenue by product, ROI timeline
2. **Comparison view**: Technified milpa vs traditional (10x improvement)
3. **Sensitivity analysis**: Yield variations at ±20% survival rates

## AI Agent Best Practices
- **Preserve Spanish domain terms** - essential for end-user communication with agronomists
- **Show intermediate calculations** when modifying yields - helps validate agronomic logic
- **Reference SPCM data** from conversation file when explaining yield assumptions
- **Avoid over-engineering** - stakeholders prefer simple scripts over complex frameworks
- **Validate against real-world constraints** - flag unrealistic parameters before running calculations
- **Document assumptions clearly** - especially when extending beyond SPCM research scope
