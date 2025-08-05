from typing import List, Tuple, Dict
import json

def max_panels(panel_w: int, panel_h: int, roof_w: int, roof_h: int) -> int:
    max_count = 0
    for i in range(roof_h // panel_h + 1):
        used_height = i * panel_h
        remaining_height = roof_h - used_height
        vertical_panels = i * (roof_w // panel_w)
        horizontal_panels = (remaining_height // panel_w) * (roof_w // panel_h)
        max_count = max(max_count, vertical_panels + horizontal_panels)
    return max_count


def calculate_panels(panel_width: int, panel_height: int, 
                     roof_width: int, roof_height: int) -> int:
    return max(
        max_panels(panel_width, panel_height, roof_width, roof_height),
        max_panels(panel_height, panel_width, roof_width, roof_height)
    )


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
