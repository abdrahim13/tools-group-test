

// Debounce function to limit the number of times a function is called
export function debounce(func: (...args: any[]) => void, delay: number = 300) {
  let timeoutId: number;

  return function (...args: any[]) {
    // Clear the previous timeout
    clearTimeout(timeoutId);

    // Set a new timeout
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  };
}