
import dayjs from 'dayjs';

export function readableDate(date: string) {
  return dayjs(date).format('DD MMMM YYYY [at] HH:mm')
}